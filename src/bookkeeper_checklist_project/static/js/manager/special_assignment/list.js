"use strict";

import { DataTableHelper } from "../../utils/datatable-helper.js";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  new DataTableHelper({
    tableID: "managerBookkeepersTable",
    customColumnsWidthObj: [{ width: "30%", targets: 0 }],
  });
});
