// Set dimensions and margins for the chart

const margin = { top: 70, right: 30, bottom: 40, left: 80 };
const width = 800 - margin.left - margin.right;
const height = 500 - margin.top - margin.bottom;

// Set up the x and y scales
const x = d3.scaleTime()
  .range([0, width]);

const y = d3.scaleLinear()
  .range([height, 0]);

function LineChart(datax, datay){
  // Create the SVG element and append it to the chart container
const svg = d3.select("#chart-container")
.append("svg")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
.append("g")
  .attr("transform", `translate(${margin.left},${margin.top})`);

// loop through inputs to make dataset using for loops 
// Create a fake dataset
const dataset = [
{ date: new Date("2022-01-01"), value: 200 },
{ date: new Date("2022-02-01"), value: 250 },
{ date: new Date("2022-03-01"), value: 180 },
{ date: new Date("2022-04-01"), value: 300 },
{ date: new Date("2022-05-01"), value: 280 },
{ date: new Date("2022-06-01"), value: 220 },
{ date: new Date("2022-07-01"), value: 300 },
{ date: new Date("2022-08-01"), value: 450 },
{ date: new Date("2022-09-01"), value: 280 },
{ date: new Date("2022-10-01"), value: 600 },
{ date: new Date("2022-11-01"), value: 780 },
{ date: new Date("2022-12-01"), value: 320 }
];

// Define the x and y domains
x.domain(d3.extent(dataset, d => d.date));
y.domain([0, d3.max(dataset, d => d.value)]);

// Add the x-axis
svg.append("g")
.attr("class", "x-axis")
.attr("transform", `translate(0,${height})`)
.call(d3.axisBottom(x))
.selectall("text")
.attr("y", -5)
.attr("x", -130)
.style("text-anchor", "middle")
.attr("transform", "rotate(-90)")
.text("Years")

// Add the y-axis
svg.append("g")
.attr("class", "y-axis")
.call(d3.axisLeft(y).ticks(5))
.selectall("text")
.attr("y", 6)
.attr("dy","1em")
.style("text-anchor", "middle")
.text("Exports")

// Create the line generator
var line = d3.line()
.x(d => x(d.date))
.y(d => y(d.value));

// Add the line path to the SVG element
svg.append("path")
.datum(dataset)
.attr("fill", "none")
.attr("stroke", "steelblue")
.attr("stroke-width", 1)
.attr("d", line);
}

// call function
LineChart(datax,datay);
