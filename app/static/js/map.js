const Mapsetup = () =>
  Promise.all([ // executes multiples promises in parallel that returns a promise when everything is resolved
    d3.tsv('https://unpkg.com/world-atlas@1.1.4/world/50m.tsv'), // promise for tsv
    d3.json('https://unpkg.com/world-atlas@1.1.4/world/50m.json') // promise for topojson
  ]).then(([tsvData, topojsonData]) => { // resolves to array of values
    const countries = topojson.feature(topojsonData, topojsonData.objects.countries);
    //search up country name by id
    const countryName = {};
    tsvData.forEach(d => { // loop through tsv file 
      countryName[d.iso_n3] = [d.name, Math.floor(Math.random() * 10)]; // set each Id with a array of [name, export_value]
    });

    countries.features.forEach(d => {
      Object.assign(d.properties, countryName[d.id]);
    });
    console.log(countryName);

    return countries;
  });

const svg = d3.select('svg');

// projection type for the map
const projection = d3.geoMercator()
const pathGenerator = d3.geoPath().projection(projection);

// group for color legend
const colorLegendG = svg.append('g')
  .attr('transform', 'translate(180,150');

const g = svg.append('g');

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

  // use topojson library to convert topojson to geojson for d3
  g.selectAll('path').data(countries.features)
    .enter().append('path')
    .attr('class', 'country')
    .attr('d', pathGenerator) // helps draw borders by setting 'd' attribute to country coordinates
    .attr('fill', d => colorScale(colorValue(d)))
    .append('title').text(d => d.properties[0] + ": " + colorValue(d)); // label selection with country name
});

