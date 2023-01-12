"use strict";

import { DataTableHelper } from "../../utils/datatable-helper.js";

document.addEventListener("DOMContentLoaded", (ev) => {
  /*
    the browser fully loaded HTML, and the DOM tree is built, but external resources like pictures <img> and stylesheets may not yet have loaded.
    */
  new DataTableHelper({
    tableID: "managerAssistantTable",
  });
});
