"use strict";

document.addEventListener("DOMContentLoaded", (ev) => {
  /*
    the browser fully loaded HTML, and the DOM tree is built, but external resources like pictures <img> and stylesheets may not yet have loaded.
    */
  const ths = document.querySelectorAll("#managerBookkeepersTable thead tr th");
  const bookkeepersTable = $("#managerBookkeepersTable").DataTable({
    autoWidth: true,
    processing: true,
    order: [], // this to disable initial order
    columnDefs: [
      // { width: "30%", targets: 0 },
      { targets: ths.length - 1, orderable: false },
    ],

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
    responsive: true,
    dom: "Bfrtip",
    buttons: [
      // "copy",
      "csv",
      "pdf",
    ],
  });
});
