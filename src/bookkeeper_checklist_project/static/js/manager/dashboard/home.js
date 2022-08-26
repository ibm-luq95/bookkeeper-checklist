"use strict";

document.addEventListener("readystatechange", (ev) => {
  // The document is still loading.
  /* if (document.readyState === "loading") {

    } */

  // The document has finished loading and the document has been parsed but sub-resources such as scripts, images, stylesheets and frames are still loading.
  /* if (document.readyState === "interactive") {

    } */

  // check if the page fully loaded with all resources
  if (document.readyState === "complete") {
    const clientChartElement = document.querySelector("#clientChart");
    const clientChart = new Chart(clientChartElement, {
      type: "line",
      data: {
        labels: ["Africa", "Asia", "Europe", "Latin America", "North America"],
        datasets: [
          {
            label: "Clients",
            backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850"],
            data: [2478, 5267, 734, 784, 433],
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        legend: { display: false },
        title: {
          display: true,
          text: "Clients (millions) in 2050",
        },
      },
    });
    // second chart
    const tasksChartElement = document.querySelector("#tasksChart");
    const tasksChart = new Chart(tasksChartElement, {
      type: "doughnut",
      data: {
        labels: ["Africa", "Asia"],
        datasets: [
          {
            label: "Tasks",
            backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850"],
            data: [2478, 5267],
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        legend: { display: false },
        title: {
          display: true,
          text: "Predicted world population (millions) in 2050",
        },
      },
    });
  }
});
