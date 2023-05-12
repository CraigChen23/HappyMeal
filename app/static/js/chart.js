// Line graph
var line = document.getElementById("line-chart");
var lineChart = new Chart(line,{
    type: 'line', // type of chart used
    data: {
        labels: ["year1", "year2", "year3","year4","year5"], // x-axis
        datasets: [
            {
                label: "Coffee Exports Line-graph", 
                data:[1,2,3,4,5], // value corresponding to labels in dataset
            }
        ]
    }
});

// Bar graph
var bar = document.getElementById("bar-chart");
var barChart = new Chart(bar,{
    type: 'bar',
    data: {
        labels: ["year1", "year2", "year3","year4","year5"], // x-axis
        datasets: [
            {
                label: "yes",
                data:[68,25,92,44,13], // value corresponding to labels in dataset
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(255, 205, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                  ],
                  borderColor: [
                    'rgb(255, 99, 132)',
                    'rgb(255, 159, 64)',
                    'rgb(255, 205, 86)',
                    'rgb(75, 192, 192)',
                    'rgb(54, 162, 235)',
                  ],
                  borderWidth: 1
            }
        ]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

// Pie chart
var pie = document.getElementById("pie-chart");
var pieChart = new Chart(pie,{
    type: 'doughnut', // type of chart used
    data: {
        labels: ["year1", "year2", "year3","year4","year5"], // x-axis
        datasets: [
            {
                label: "Nice", 
                data:[1,2,3,4,5], // value corresponding to labels in dataset
            }
        ],
        hoverOffset: 10
    },
});
