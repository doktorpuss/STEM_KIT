import tkinter as tk
from tkinter import messagebox
import subprocess

class DragDropCodeEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Drag & Drop Code Editor")
        
        # Canvas để kéo thả
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Khung chứa các block lệnh
        self.toolbox = tk.Frame(root, width=200, bg="#ccc")
        self.toolbox.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Nút chạy chương trình
        self.run_button = tk.Button(self.toolbox, text="Run", command=self.run_code)
        self.run_button.pack(pady=10)
        
        # Nút xóa block
        self.delete_button = tk.Button(self.toolbox, text="Delete", command=self.delete_selected_block)
        self.delete_button.pack(pady=10)
        
        # Danh sách các block lệnh với tên hiển thị và code tương ứng
        self.blocks = [
            {"name": "Print", "code": "print('{}')", "args": True},
            {"name": "Loop", "code": "for i in range({}):\n    ", "args": True, "container": True},
            {"name": "Condition", "code": "if {}:\n    ", "args": True, "container": True}
        ]
        
        self.placed_blocks = []  # Lưu các block đã đặt
        self.selected_block = None  # Lưu block đang chọn
        
        for block in self.blocks:
            btn = tk.Button(self.toolbox, text=block["name"], command=lambda b=block: self.create_draggable_block(b))
            btn.pack(pady=5, fill=tk.X)
        
        self.drag_data = {"item": None, "x": 0, "y": 0, "items": []}  # Lưu trạng thái kéo thả
    
    def create_draggable_block(self, block):
        y_position = len(self.placed_blocks) * 50 + 20
        block_id = self.canvas.create_rectangle(20, y_position, 180, y_position + 30, fill="lightblue", tags="block")
        text_id = self.canvas.create_text(100, y_position + 15, text=block["name"], tags="block")
        
        entry = None
        entry_id = None
        if block["args"]:
            entry = tk.Entry(self.canvas)
            entry_id = self.canvas.create_window(200, y_position + 15, window=entry, width=100, height=20)
        
        container_id = None
        if "container" in block and block["container"]:
            container_id = self.canvas.create_rectangle(40, y_position + 30, 160, y_position + 80, outline="black", dash=(4, 2))
        
        self.placed_blocks.append((block, block_id, text_id, entry, entry_id, container_id))
        
        self.canvas.tag_bind(block_id, "<ButtonPress-1>", self.on_drag_start)
        self.canvas.tag_bind(text_id, "<ButtonPress-1>", self.on_drag_start)
        if entry_id:
            self.canvas.tag_bind(entry_id, "<ButtonPress-1>", self.on_drag_start)
        
        self.canvas.tag_bind(block_id, "<B1-Motion>", self.on_drag_motion)
        self.canvas.tag_bind(text_id, "<B1-Motion>", self.on_drag_motion)
        if entry_id:
            self.canvas.tag_bind(entry_id, "<B1-Motion>", self.on_drag_motion)
        
        self.canvas.tag_bind(block_id, "<ButtonRelease-1>", self.on_drag_end)
        self.canvas.tag_bind(text_id, "<ButtonRelease-1>", self.on_drag_end)
        if entry_id:
            self.canvas.tag_bind(entry_id, "<ButtonRelease-1>", self.on_drag_end)
        
        self.drag_data["items"].append((block_id, text_id, entry_id, container_id))
    
    def on_drag_start(self, event):
        item = self.canvas.find_closest(event.x, event.y)[0]
        self.drag_data["item"] = item
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y
        
        for block_data in self.drag_data["items"]:
            if item in block_data:
                self.drag_data["current_block"] = block_data
                self.selected_block = block_data
                break
    
    def on_drag_motion(self, event):
        if self.drag_data["item"] and "current_block" in self.drag_data:
            dx = event.x - self.drag_data["x"]
            dy = event.y - self.drag_data["y"]
            
            for item in self.drag_data["current_block"]:
                if item:
                    self.canvas.move(item, dx, dy)
            
            self.drag_data["x"] = event.x
            self.drag_data["y"] = event.y
    
    def on_drag_end(self, event):
        self.drag_data["item"] = None
        self.drag_data.pop("current_block", None)
    
    def delete_selected_block(self):
        if self.selected_block:
            for item in self.selected_block:
                if item:
                    self.canvas.delete(item)
            self.placed_blocks = [b for b in self.placed_blocks if b != self.selected_block]
            self.drag_data["items"] = [b for b in self.drag_data["items"] if b != self.selected_block]
            self.selected_block = None
    
    def run_code(self):
        code_lines = []
        for block, block_id, text_id, entry, entry_id, container_id in self.placed_blocks:
            if block["args"] and entry:
                arg_value = entry.get().strip()
                if not arg_value:
                    messagebox.showerror("Error", "Missing argument for a block!")
                    return
                code_lines.append(block["code"].format(arg_value))
            else:
                code_lines.append(block["code"])
        
        code = "\n".join(code_lines)
        
        with open("generated_script.py", "w") as f:
            f.write(code)
        
        try:
            result = subprocess.run(["python", "generated_script.py"], check=True, capture_output=True, text=True)
            messagebox.showinfo("Output", result.stdout)
        except subprocess.CalledProcessError as e:
            with open("error.log", "w") as log:
                log.write(e.stderr)
            messagebox.showerror("Error", f"Code Execution Failed. Check 'error.log' for details.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DragDropCodeEditor(root)
    root.mainloop()
