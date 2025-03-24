Blockly.Blocks['print'] = {
  init: function () {
      this.appendValueInput("TEXT")
          .setCheck("String")
          .appendField("print");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(160);
      this.setTooltip("In ra màn hình");
      this.setHelpUrl("");
  }
};

Blockly.Blocks['input'] = {
  init: function () {
      this.appendDummyInput()
          .appendField("input")
          .appendField(new Blockly.FieldTextInput("Nhập dữ liệu"), "PROMPT");
      this.setOutput(true, "String");
      this.setColour(160);
      this.setTooltip("Nhận dữ liệu từ bàn phím");
      this.setHelpUrl("");
  }
};

Blockly.Blocks['math_arithmetic'] = {
  init: function () {
      this.appendValueInput("A")
          .setCheck("Number");
      this.appendDummyInput()
          .appendField(new Blockly.FieldDropdown([
              ["+", "ADD"],
              ["-", "MINUS"],
              ["×", "MULTIPLY"],
              ["÷", "DIVIDE"]
          ]), "OP");
      this.appendValueInput("B")
          .setCheck("Number");
      this.setInputsInline(true);
      this.setOutput(true, "Number");
      this.setColour(230);
      this.setTooltip("Phép toán số học");
      this.setHelpUrl("");
  }
};

Blockly.Blocks['if_else'] = {
  init: function () {
      this.appendValueInput("CONDITION")
          .setCheck("Boolean")
          .appendField("nếu");
      this.appendStatementInput("DO")
          .setCheck(null)
          .appendField("thì");
      this.appendStatementInput("ELSE")
          .setCheck(null)
          .appendField("khác");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(210);
      this.setTooltip("Cấu trúc điều kiện If-Else");
      this.setHelpUrl("");
  }
};

Blockly.Blocks['for_loop'] = {
  init: function () {
      this.appendDummyInput()
          .appendField("lặp từ")
          .appendField(new Blockly.FieldVariable("i"), "VAR")
          .appendField("trong khoảng")
          .appendField(new Blockly.FieldNumber(0, 0), "START")
          .appendField("đến")
          .appendField(new Blockly.FieldNumber(10, 0), "END");
      this.appendStatementInput("DO")
          .setCheck(null)
          .appendField("thực hiện");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(120);
      this.setTooltip("Vòng lặp for");
      this.setHelpUrl("");
  }
};
