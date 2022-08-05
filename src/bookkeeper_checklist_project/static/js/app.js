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

    document.querySelectorAll(".tablinks").forEach((element) => {
      element.addEventListener("click", (event) => {
        let i, tabcontent, tablinks;
        const clickedBtn = event.currentTarget;
        const data = clickedBtn.dataset;
        const tabContentId = data["tabElement"];
        tabcontent = document.querySelectorAll(".tabcontent");
        tabcontent.forEach((tabElement) => {
          tabElement.style.display = "none";
        });
        tablinks = document.querySelectorAll(".tablinks");
        tablinks.forEach((linkElement) => {
          linkElement.className = linkElement.className.replace("active", "");
        });
        document.querySelector(`#${tabContentId}`).style.display = "block";
        clickedBtn.classList.add("active");
      });
    });

    // Get the element with id="defaultOpen" and click on it
    document.getElementById("defaultOpen").click();

    const acc = document.querySelectorAll(".accordion");
    let i;
    for (i = 0; i < acc.length; i++) {
      acc[i].addEventListener("click", function () {
        this.classList.toggle("active");
        let panel = this.nextElementSibling;
        if (panel.style.maxHeight) {
          panel.style.maxHeight = null;
        } else {
          panel.style.maxHeight = panel.scrollHeight + "px";
        }
      });
    }
  }
});
