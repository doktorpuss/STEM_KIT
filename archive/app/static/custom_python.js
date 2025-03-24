Blockly.Python['print'] = function (block) {
  var value_text = Blockly.Python.valueToCode(block, 'TEXT', Blockly.Python.ORDER_NONE) || "''";
  return 'print(' + value_text + ')\n';
};

Blockly.Python['input'] = function (block) {
  var prompt = block.getFieldValue('PROMPT');
  return ['input("' + prompt + '")', Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python['math_arithmetic'] = function (block) {
  var operator = block.getFieldValue('OP');
  var op_map = { "ADD": "+", "MINUS": "-", "MULTIPLY": "*", "DIVIDE": "/" };
  var value_a = Blockly.Python.valueToCode(block, 'A', Blockly.Python.ORDER_ATOMIC) || '0';
  var value_b = Blockly.Python.valueToCode(block, 'B', Blockly.Python.ORDER_ATOMIC) || '0';
  return [value_a + " " + op_map[operator] + " " + value_b, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python['if_else'] = function (block) {
  var condition = Blockly.Python.valueToCode(block, 'CONDITION', Blockly.Python.ORDER_NONE) || 'False';
  var statements_do = Blockly.Python.statementToCode(block, 'DO') || 'pass';
  var statements_else = Blockly.Python.statementToCode(block, 'ELSE') || 'pass';
  return "if " + condition + ":\n" + Blockly.Python.prefixLines(statements_do, "    ") +
         "else:\n" + Blockly.Python.prefixLines(statements_else, "    ");
};

Blockly.Python['for_loop'] = function (block) {
  var variable = Blockly.Python.variableDB_.getName(block.getFieldValue('VAR'), Blockly.Variables.NAME_TYPE);
  var start = block.getFieldValue('START');
  var end = block.getFieldValue('END');
  var statements = Blockly.Python.statementToCode(block, 'DO') || 'pass';
  return "for " + variable + " in range(" + start + ", " + end + "):\n" + Blockly.Python.prefixLines(statements, "    ");
};
