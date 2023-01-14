"use strict";

import { DataTableHelper } from "../../utils/datatable-helper.js";

document.addEventListener("readystatechange", (ev) => {
  const checkBookkeeperSpecialAssignmentsTable = document.querySelector(
    "table#bookkeeperSpecialAssignmentsTable"
  );
  if (checkBookkeeperSpecialAssignmentsTable) {
    new DataTableHelper({
      tableID: "bookkeeperSpecialAssignmentsTable",
    });
  }

  const checkBookkeeperRequestedSpecialAssignmentsTable =
    document.querySelector("table#bookkeeperRequestedSpecialAssignmentsTable");
  if (checkBookkeeperRequestedSpecialAssignmentsTable) {
    new DataTableHelper({
      tableID: "bookkeeperRequestedSpecialAssignmentsTable",
    });
  }
});
