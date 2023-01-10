"use strict";

/**
 * This will be the helper to datatable.js list view
 */
class DataTableHelper {
  /**
   * Constructor which will init data table js table
   * @param {string} tableID Datatable DOM id
   * @param {bool} isStateSave Save last state of order in the table
   * @param {bool} isAutoWidth Auto width table
   * @param {bool} disableDefaultOrder Disable auto order for data table js
   */
  constructor({
    tableID,
    isStateSave = false,
    isAutoWidth = true,
    disableDefaultOrder = true,
    customColumnsWidthObj = null,
  }) {
    this.tableID = `#${tableID}`;
    this.isAutoWidth = isAutoWidth;
    this.isStateSave = isStateSave;
    this.disableDefaultOrder = disableDefaultOrder;
    this.columnsThElements = document.querySelectorAll(
      `${this.tableID} thead tr th`
    );
    this.tableOptions = {};
    this.lastIndexThNumber = this.columnsThElements.length - 1;
    this.customColumnsWidthObj = customColumnsWidthObj;

    // call initialize data table js method
    this.initDataTable();
  }

  /**
   * This will init the data table js
   */
  initDataTable() {
    this.tableOptions = {
      responsive: true,
      autoWidth: this.isAutoWidth,
      processing: true,
      fixedHeader: true,
      fixedColumns: true,
      dom: "Bfrtip",
      buttons: [
        // "copy",
        "csv",
        "pdf",
      ],
      columnDefs: [
        // { width: "1%", targets: 0 },
        { targets: this.lastIndexThNumber, orderable: false },
      ],
    };
    // check if disable default order
    if (this.disableDefaultOrder === true) {
      this.tableOptions["order"] = [];
    }

    // check if save state is true
    if (this.isStateSave === true) {
      this.tableOptions["stateSave"] = true;
      this.tableOptions["stateSaveCallback"] = (settings, data) => {
        localStorage.setItem(
          "DataTables_" + settings.sInstance,
          JSON.stringify(data)
        );
      };
      this.tableOptions["stateLoadCallback"] = (settings) =>
        JSON.parse(localStorage.getItem("DataTables_" + settings.sInstance));
    }

    // check if custom column width passed
    if (this.customColumnsWidthObj) {
      for (const colWidth of this.customColumnsWidthObj) {
        this.tableOptions["columnDefs"].push(colWidth);
      }
    }
    // call DataTable object
    new DataTable(this.tableID, this.tableOptions);
    // $(this.tableID).DataTable(this.tableOptions);
  }
}

export { DataTableHelper };
