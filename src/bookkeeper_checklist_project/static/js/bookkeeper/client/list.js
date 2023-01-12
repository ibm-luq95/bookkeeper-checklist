"use strict";

import { DataTableHelper } from "../../utils/datatable-helper.js";

document.addEventListener("readystatechange", (ev) => {
  new DataTableHelper({
    tableID: "bookkeeperClientsJobsTable",
  });
});
