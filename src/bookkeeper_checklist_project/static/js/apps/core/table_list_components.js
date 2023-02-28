"use strict";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const tableCompElements = document.querySelector("table.table-list-comp");
  if (tableCompElements) {
    const theadElement = tableCompElements.querySelector("thead");
    const thCellElements = theadElement.querySelectorAll("th");
    const total = thCellElements.length;
    const isEmptyElement = tableCompElements.querySelector("tr.is-empty");
    if (isEmptyElement) {
      const tdEmptyElement = isEmptyElement.querySelector("td");
      tdEmptyElement.setAttribute("colspan", total);
    }
  }
});
