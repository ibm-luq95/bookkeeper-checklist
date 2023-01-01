"use strict";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
    const clientsTable = $("#specialAssignmentsTable").DataTable({
        autoWidth: true,
        processing: true,
        // "info": false,
        // "paging": false,
        // stateSave: true,
        stateSaveCallback: function (settings, data) {
          localStorage.setItem("DataTables_" + settings.sInstance, JSON.stringify(data));
        },
        stateLoadCallback: function (settings) {
          return JSON.parse(localStorage.getItem("DataTables_" + settings.sInstance));
        },
        fixedHeader: true,
        responsive: true,
        dom: "Bfrtip",
        buttons: [
          // "copy",
          "csv",
          "pdf",
        ],
      });
});
