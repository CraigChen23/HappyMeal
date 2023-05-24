// Set dimensions and margins for the chart
const margin = { top: 70, right: 30, bottom: 40, left: 80 };
const width = screen.width - margin.left - margin.right;
const height = 650 - margin.top - margin.bottom;

// Set up the x and y scales
const x = d3.scaleTime()
  .range([0, width]);

const y = d3.scaleLinear()
  .range([height, 0]);

const YearsToExport = []
for(let i=0; i<years.length; i++){
  var a = {}
  if (exportAmt[i] != undefined){
    a = {xvalue: years[i], yvalue: exportAmt[i]};
  }else{
    a = {xvalue: years[i], yvalue: 0};
  }
  YearsToExport.push(a);
}

console.log(YearsToExport)

  
function LineChart(data){
  // Create the SVG element and append it to the chart container
const svg = d3.select("#chart-container")
.append("svg")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
.append("g")
  .attr("transform", `translate(${margin.left},${margin.top})`);

// Define the x and y domains
var x = d3.scaleBand()
.domain(data.map(d => d.xvalue))
.range([0, width - margin.left - margin.right])
.padding(.1);

var y = d3.scaleLinear()
.domain([0, d3.max(data, d => d.yvalue * 1.05)])
.range([height - margin.top - margin.bottom, 0])
.nice();

console.log(d3.max(data, d => d.yvalue))

// Add the x-axis to the chart

svg.append("g")
.attr("class", "x axis")
.attr("transform", "translate(0," + (height - margin.top - margin.bottom) + ")")
.call(d3.axisBottom(x))
.selectAll("text")
  .attr("y", -2)
  .attr("x", -25)
  .attr("dx", "0.2em")
  .style("text-anchor", "middle")
  .attr("transform", "rotate(-90)")

// Add the y-axis to the chart
svg.append("g")
.attr("class", "y axis")
.call(d3.axisLeft(y).ticks(10))
.append("text")
  .attr("transform", "rotate(-90)")
  .attr("x", -6)
  .attr("y", 6)
  .attr("dy", "1em")
  .style("text-anchor", "midde")

// Add the line to the chart
var line = d3.line()
.x(d => x(d.xvalue) + x.bandwidth() / 2)
.y(d => y(d.yvalue));

// Add the line path to the SVG element
svg.append("path")
.datum(data)
.attr("fill", "none")
.attr("stroke", "steelblue")
.attr("stroke-width", 1.5)
.attr("d", line);
}
// call function
LineChart(YearsToExport);
console.log(YearsToExport)
