"use strict";
import { DataTableHelper } from "../../../utils/datatable-helper.js";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const segJobTable = document.querySelector("table#segJobTable");
  if (segJobTable) {
    const dataTableHelper = new DataTableHelper({
      tableID: "segJobTable",
    });
  }
});
