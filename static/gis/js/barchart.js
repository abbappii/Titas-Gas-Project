// function barChart(xVal, yVal) {
//     var xValues = xVal;
//     var yValues = yVal;
//     var barColors = [
//         "#b91d47",
//         "#00aba9",
//         "#2b5797",
//         "#e8c3b9",
//         "#1e7145",
//         "#b91d47",
//         "#00aba9",
//         "#2b5797",
//         "#e8c3b9",
//         "#1e7145",
//         "#b91d47",
//         "#00aba9",
//         "#2b5797",
//         "#e8c3b9",
//         "#1e7145"
//     ];
//
//     new Chart("myChart", {
//         type: "pie",
//         data: {
//             labels: xValues,
//             datasets: [{
//                 backgroundColor: barColors,
//                 data: yValues
//             }]
//         },
//         options: {
//             title: {
//                 display: true,
//                 text: "Gas Line BarChart"
//             }
//         }
//     });
// }

function barChart(xVal, yVal) {
    var xArray = xVal;
    var yArray = yVal;

    var layout = {title: "Gas Pipeline"};

    var data = [{labels: xArray, values: yArray, type: "pie"}];

    Plotly.newPlot("myPlot", data, layout);
}