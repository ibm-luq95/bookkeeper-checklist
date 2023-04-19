"use strict";
import { enableInputsOnLoad } from "./utils/helpers.js";
document.addEventListener("readystatechange", (ev) => {
  // // The document is still loading.
  // if (document.readyState === "loading") {

  // }

  // // The document has finished loading and the document has been parsed but sub-resources such as scripts, images, stylesheets and frames are still loading.
  // if (document.readyState === "interactive") {

  // }

  // check if the page fully loaded with all resources
  if (document.readyState === "complete") {
    // init clipboard.js lib
    // new ClipboardJS(".copyBtn");
    enableInputsOnLoad("bkchlst-input");
    const burger = document.querySelector(".burger");
    const menu = document.querySelector("#" + burger.dataset.target);
    const dropdown = document.querySelector(".dropdown");

    dropdown.addEventListener("click", function (event) {
      event.stopPropagation();
      dropdown.classList.toggle("is-active");
    });
    burger.addEventListener("click", function () {
      burger.classList.toggle("is-active");
      menu.classList.toggle("is-active");
    });

    // Return an array of bulmaCollapsible instances (empty if no DOM node found)
    // const bulmaCollapsibleInstances = bulmaCollapsible.attach(".is-collapsible", {
    //   expand: false,
    // });

    // Loop into instances
    /* bulmaCollapsibleInstances.forEach((bulmaCollapsibleInstance) => {
      // Check if current state is collapsed or not
      console.log(bulmaCollapsibleInstance.collapsed());
    }); */

    // add is-active to left side a elements
    const leftSideActiveElement = document.querySelector("a.left-side-item.is-active");
    const leftSideElements = document.querySelectorAll("a.left-side-item");
    // console.log(leftSideElements);
    leftSideElements.forEach((element) => {
      element.addEventListener("click", (event) => {
        const currentTarget = event.currentTarget;
        leftSideActiveElement.classList.remove("is-active");
        // console.log("click");
        currentTarget.classList.add("is-active");
      });
    });

    // disabled anchor elements
    const disabledAnchorElements = document.querySelectorAll("a.disabledAnchorElement");
    if (disabledAnchorElements) {
      disabledAnchorElements.forEach((element) => {
        element.addEventListener("click", (event) => {
          event.preventDefault();
        });
      });
    }

    const triggers = document.querySelectorAll(".dropdown .dropdown-trigger");

    triggers.forEach(function (trigger) {
      let isOpen = false;
      trigger.addEventListener("click", function () {
        if (isOpen) {
          trigger.parentElement.classList.remove("is-active");
          isOpen = false;
        } else {
          trigger.parentElement.classList.add("is-active");
          isOpen = true;
        }
      });
    });

    // tinymce.init({
    //   selector: ".rich-textarea", // change this value according to your HTML
    //   placeholder: "Type here...",
    //   highlight_on_focus: true,
    //   plugins: ["advlist", "autolink", "link", "image", "lists"],
    //   // content_security_policy: "default-src 'self'",
    //   content_security_policy: "style-src 'self' 'unsafe-inline';",
    //   referrer_policy: "origin",
    //   // referrer_policy: "strict-origin-when-cross-origin",
    //   // content_security_policy: "default-src 'self'",
    //   xss_sanitization: true,
    //   resize: "both",
    //   // menubar: false,
    //   // removed_menuitems: 'file redo'
    //   menubar: 'edit insert view format table tools help',
    //   // toolbar: false,
    //   // height: 300,
    //   // width: 300,
    // });

    const dropdowns = document.querySelectorAll(".dropdown:not(.is-hoverable)");

    /*
     * Close dropdowns by removing `is-active` class.
     */
    function closeDropdowns() {
      dropdowns.forEach(function (el) {
        el.classList.remove("is-active");
      });
    }
    // Close dropdowns if ESC pressed
    document.addEventListener("keydown", function (event) {
      let e = event || window.event;
      if (e.key === "Esc" || e.key === "Escape") {
        closeDropdowns();
      }
    });

    // document.addEventListener("click", function (e) {
    //   // closeDropdowns();
    //   console.log(e.target);
    //   // dropdowns.forEach(function (el) {
    //   //   el.classList.remove("is-active");
    //   // });
    // });

    function closeModal($el) {
      $el.classList.remove("is-active");
    }
    (document.querySelectorAll(".notification .delete") || []).forEach(($delete) => {
      const $notification = $delete.parentNode;

      $delete.addEventListener("click", () => {
        $notification.parentNode.removeChild($notification);
      });
    });

    // bulma css modal js

    // Add a click event on various child elements to close the parent modal
    (
      document.querySelectorAll(
        ".modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .close-modal-btn",
      ) || []
    ).forEach(($close) => {
      const $target = $close.closest(".modal");

      $close.addEventListener("click", () => {
        closeModal($target);
      });
    });

    // Add a keyboard event to close all modals
    document.addEventListener("keydown", (event) => {
      const e = event || window.event;

      if (e.keyCode === 27) {
        // Escape key
        closeAllModals();
      }
    });
    const allSelectizeElements = document.querySelectorAll("select.selectize");
    if (allSelectizeElements) {
      allSelectizeElements.forEach((element) => {
        NiceSelect.bind(element);
      });
    }
  }
});
