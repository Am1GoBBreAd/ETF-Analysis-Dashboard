function main(workbook: ExcelScript.Workbook) {
  let sheet = workbook.getWorksheet("Inputs_block_trade");
  const threshold = 250000;

  // 1. Define Output Location (Columns U and V)
  const outputHeaderCol = 20; // Column U
  const outputValueCol = 21;  // Column V

  // 2. Clear previous results and set up Headers
  sheet.getRange("U:V").clear();
  sheet.getCell(0, outputHeaderCol).setValue("Equity");
  sheet.getCell(0, outputValueCol).setValue("#Trades >= 250,000");

  let headerRange = sheet.getRangeByIndexes(0, outputHeaderCol, 1, 2);
  headerRange.getFormat().getFont().setBold(true);
  headerRange.getFormat().getFill().setColor("#D3D3D3");

  /**
   * 3. Define mapping based on image:
   * A, B, C: Headers in Row 1, Volume in Cols B, E, H
   * D, E, F: Headers in Row 1, Volume in Cols K, N, Q
   * Data rows: Row 2 to 49
   */
  const tickerConfigs = [
    { nameLoc: "C1", dataRange: "C2:C100" }, // A CN EQUITY
    { nameLoc: "F1", dataRange: "F2:F100" }, // B CN EQUITY
    { nameLoc: "I1", dataRange: "I2:I100" }, // C CN EQUITY
    { nameLoc: "M1", dataRange: "M2:M100" }, // D CN EQUITY
    { nameLoc: "P1", dataRange: "P2:P49" }, // E CN EQUITY
    { nameLoc: "S1", dataRange: "S2:S100" }  // F CN EQUITY
  ];

  tickerConfigs.forEach((config, index) => {
    // Get the actual Ticker Name (e.g., "A CN EQUITY")
    let tickerName = sheet.getRange(config.nameLoc).getValue() as string;

    // Get the Volume values
    let values = sheet.getRange(config.dataRange).getValues();

    let count = 0;
    for (let i = 0; i < values.length; i++) {
      let val = values[i][0];
      // Only count numbers that meet the threshold
      if (typeof val === "number" && val >= threshold) {
        count++;
      }
    }

    // 4. Place final results in U and V
    sheet.getCell(index + 1, outputHeaderCol).setValue(tickerName);
    sheet.getCell(index + 1, outputValueCol).setValue(count);
  });

  sheet.getRange("U:V").getFormat().autofitColumns();
}
