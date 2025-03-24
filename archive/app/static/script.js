// Khởi tạo Blockly
var workspace = Blockly.inject('blocklyDiv', {
    toolbox: `<xml>
                <block type="controls_if"></block>
                <block type="logic_compare"></block>
                <block type="math_number"></block>
                <block type="text"></block>
                <block type="text_print"></block>
              </xml>`
});

// Cập nhật mã Python khi thay đổi khối lệnh
function generateCode() {
    var code = Blockly.Python.workspaceToCode(workspace);
    document.getElementById("codeArea").value = code;
}

// Gửi mã Python lên server để chạy trong terminal
function runCode() {
    var code = document.getElementById("codeArea").value;

    fetch('/run', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code: code })
    }).then(response => response.text())
      .then(output => alert(output))  // Hiển thị thông báo từ server
      .catch(error => console.error('Error:', error));
}

// Tải mã Python về file `.py`
function downloadCode() {
    var code = document.getElementById("codeArea").value;
    var blob = new Blob([code], { type: "text/python" });
    var link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "generated_code.py";
    link.click();
}

// Lắng nghe thay đổi trong Blockly để cập nhật mã Python
workspace.addChangeListener(generateCode);
