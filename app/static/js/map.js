const Mapsetup = () =>
  Promise.all([ // executes multiples promises in parallel that returns a promise when everything is resolved
    d3.tsv('https://unpkg.com/world-atlas@1.1.4/world/50m.tsv'), // promise for tsv
    d3.json('https://unpkg.com/world-atlas@1.1.4/world/50m.json') // promise for topojson
  ]).then(([tsvData, topojsonData]) => { // resolves to array of values
    const countries = topojson.feature(topojsonData, topojsonData.objects.countries);
    //search up country name by id
    const countryName = {};
    tsvData.forEach(d => { // loop through tsv file
      //var dbList = document.getElementById("exports").innerHTML;
      //console.log((dbList));
      //dbList = JSON.parse(dbList)
      //countryName[d.iso_n3] = [d.name, Math.floor(dbList[countryName])]; // set each Id with a array of [name, export_value]
      //console.log(dbList[countryName]);
      countryName[d.iso_n3] = [d.name, Math.floor(Math.random() * 10)];
    });

    //console.log(countryName)

    /*
    // -------------------- YO START HERE BRO (CHECK CONSOLE)------------------------------
    // data manipulation in progress
    const temp = {};
    for (keys in countryName){
      for (var i = 0; i < DataByYears.length; i++){
        if (DataByYears[i][0] == countryName[keys][0]){
          temp[countryName["" + keys][0]] = [countryName[keys[0]], DataByYears[i][1] + ""]
          //countryName[keys] = [countryName[keys][0], parseFloat(DataByYears[i][1])];
        }    
      }
    }

    for (const [key, value] of Object.entries(countryName)) {
      console.log(key, value);
    }

    
    
    const temp2 = [];
    for (keys in temp){
      temp2.push("[" + keys + ":" + temp[keys] + "]")
    }
    
    console.log("Temp dict value is: " + temp2)
    // --------------------- END OF TESTS ----------------------- **/

    countries.features.forEach(d => {
      Object.assign(d.properties, countryName[d.id]);
    });
    //console.log(countryName);

    return countries;
  });

  const colorLegend = (selection, props) => {
    const {                      
      colorScale,                
      circleRadius,
      spacing,                   
      textOffset,
      backgroundRectWidth        
    } = props;                   
    
    const backgroundRect = selection.selectAll('rect')
      .data([null]);             
    const n = colorScale.domain().length; 
    backgroundRect.enter().append('rect')
      .merge(backgroundRect)
        .attr('x', -circleRadius * 2)   
        .attr('y', -circleRadius * 2)   
        .attr('rx', circleRadius * 2)   
        .attr('width', backgroundRectWidth)
        .attr('height', spacing * n + circleRadius * 2) 
        .attr('fill', 'black')
        .attr('opacity', 0.6);
    
    const groups = selection.selectAll('.tick')
      .data(colorScale.domain());
    const groupsEnter = groups
      .enter().append('g')
        .attr('class', 'tick');
    groupsEnter
      .merge(groups)
        .attr('transform', (i) =>    
          `translate(0, ${i * spacing})`  
        );
    groups.exit().remove();
    
    groupsEnter.append('circle')
      .merge(groups.select('circle')) 
        .attr('r', circleRadius)
        .attr('fill', colorScale);      
    
    groupsEnter.append('text')
      .merge(groups.select('text'))   
        .text(d => d)
        .attr('dy', '0.32em')
        .attr('x', textOffset)
  };
  
const svg = d3.select('svg');

// projection type for the map
const projection = d3.geoMercator()
const pathGenerator = d3.geoPath().projection(projection);

const g = svg.append('g');

// group for color legend
const colorLegendG = svg.append('g')
  .attr('transform', 'translate(180,150');

//zoom with scrolling
svg.call(d3.zoom().on('zoom', () => {
  g.attr('transform', d3.event.transform);
}));

const colorScale = d3.scaleOrdinal();
const colorValue = d => d.properties[1];

Mapsetup().then(countries => {
  colorScale.domain(countries.features.map(colorValue))
    .domain(colorScale.domain().sort().reverse()) // sort values greatest to least
    .range(d3.schemeSpectral[colorScale.domain().length]);
  
  colorLegendG.call(colorLegend, {
    colorScale,
    circleRadius: 10,
    spacing: 30,
    textOffset: 15,
    backgroundRectWidth: 50
  });

  // use topojson library to convert topojson to geojson for d3
  g.selectAll('path').data(countries.features)
    .enter().append('path')
    .attr('class', 'country')
    .attr('d', pathGenerator) // helps draw borders by setting 'd' attribute to country coordinates
    .attr('fill', d => colorScale(colorValue(d)))
    .append('title').text(d => d.properties[0] + ": " + colorValue(d)); // label selection with country name
});

//console.log(DataByYears)