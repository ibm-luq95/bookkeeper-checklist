"use strict";

document.addEventListener("readystatechange", (ev) => {
  $.fn.dataTable.ext.buttons.alert = {
    className: "buttons-alert",

    action: function (e, dt, node, config) {
      alert(this.text());
    },
  };
  const jobsTable = $("#tasksTable").DataTable({
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
    /* buttons: [
      {
        extend: "alert",
        text: "My button 1",
      },
      {
        extend: "alert",
        text: "My button 2",
      },
      {
        extend: "alert",
        text: "My button 3",
      },
    ], */
    buttons: ["copy", "csv", "pdf"],
  });
});
