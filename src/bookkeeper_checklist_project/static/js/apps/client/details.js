"use strict";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const links = document.querySelectorAll(".assistant-client-link");
  const sectionContentHeaderElement = document.querySelector(
    "#sectionContentHeader"
  );
  const fullUrl = window.location.href;
  const pageSection = fullUrl.substring(fullUrl.lastIndexOf("/") + 1);
  links.forEach((link) => {
    link.classList.remove("is-active");
  });
  const currentLink = document.querySelector(
    `li[data-link-name=${pageSection}]`
  );
  currentLink.classList.add("is-active");

  // set title of the current section
  sectionContentHeaderElement.textContent = currentLink.dataset["linkLabel"];

  // display the tab content
  const linkItemElement = currentLink.querySelector("a");
  const tabContentId = linkItemElement.dataset["tabElement"];
  const tabContentElement = document.querySelector(`#${tabContentId}`);
  tabContentElement.hidden = false;
});
