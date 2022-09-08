"use strict";
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
  }
});
