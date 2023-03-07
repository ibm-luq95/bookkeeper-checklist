"use strict";

import { getCookie } from "../../utils/cookie.js";
import { enableInputsOnLoad, sendRequest } from "../../utils/helpers.js";
import { showMicroModal } from "../../utils/model-box.js";
import { showToastNotification } from "../../utils/notifications.js";
document.addEventListener("readystatechange", (ev) => {
  // The document is still loading.
  /* if (document.readyState === "loading") {

    } */

  // The document has finished loading and the document has been parsed but sub-resources such as scripts, images, stylesheets and frames are still loading.
  /* if (document.readyState === "interactive") {

    } */

  // check if the page fully loaded with all resources
  if (document.readyState === "complete") {
    enableInputsOnLoad("bkchlst-input");
    const addNewJobBtn = document.querySelector("#addNewJobBtn");
    const addNewClientBtn = document.querySelector("#addNewClientBtn");
    const readonlySelectElements = document.querySelectorAll(".readonly-select");
    readonlySelectElements.forEach((element) => {
      element.addEventListener("change", (event) => {
        return false;
      });
    });
    $("#edit-preferences").click(function () {
      $("#edit-preferences-modal").addClass("is-active");
    });
    $(".modal-card-head button.delete, .modal-save, .modal-cancel").click(function () {
      $("#edit-preferences-modal").removeClass("is-active");
    });
    $("#tabs li").on("click", function () {
      const tab = $(this).data("tab");

      $("#tabs li").removeClass("is-active");
      $(this).addClass("is-active");

      $("#tab-content section").removeClass("is-active");
      $('section[data-content="' + tab + '"]').addClass("is-active");
    });

    if (addNewJobBtn) {
      addNewJobBtn.addEventListener("click", (event) => {
        showMicroModal("jobs-form-modal");
      });
    }
    if (addNewClientBtn) {
      addNewClientBtn.addEventListener("click", (event) => {
        showMicroModal("client-form-modal");
      });
    }
  }
});
