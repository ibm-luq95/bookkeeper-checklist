"use strict";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const ths = document.querySelectorAll("#specialAssignmentsTable thead tr th");
  // console.log($('#specialAssignmentsTable thead tr th').length - 1);
  const clientsTable = $("#specialAssignmentsTable").DataTable({
    autoWidth: true,
    processing: true,
    columnDefs: [
      { width: "30%", targets: 0 },
      {targets: ths.length - 1, orderable: false}
    ],
    order: [], // this to disable initial order
    // "info": false,
    // "paging": false,
    // stateSave: true,
    stateSaveCallback: function (settings, data) {
      localStorage.setItem(
        "DataTables_" + settings.sInstance,
        JSON.stringify(data)
      );
    },
    stateLoadCallback: function (settings) {
      return JSON.parse(
        localStorage.getItem("DataTables_" + settings.sInstance)
      );
    },
    fixedHeader: true,
    fixedColumns: true,
    // scrollCollapse: true,
    responsive: true,
    dom: "Bfrtip",
    buttons: [
      // "copy",
      "csv",
      "pdf",
    ],
  });
});
