const svg = d3.select('svg');

// projection type for the map
const projection = d3.geoMercator();
const pathGenerator = d3.geoPath().projection(projection);

// pass data content into a promise(object representing the eventual result of the operation)
Promise.all([ // executes multiples promises in parallel that returns a promise when everything is resolved
  d3.tsv('https://unpkg.com/world-atlas@1.1.4/world/50m.tsv'), // promise for tsv
  d3.json('https://unpkg.com/world-atlas@1.1.4/world/50m.json') // promise for topojson
]).then(([tsvData, topojsonData]) => { // resolves to array of values

    //search up country name by id
    const countryName = {};
    tsvData.forEach(d => { // loop through tsv file 
      countryName[d.iso_n3] = d.name_long;
    });

    // use topojson library to convert topojson to geojson for d3
    const countries = topojson.feature(topojsonData, topojsonData.objects.countries);
    svg.selectAll('path').data(countries.features)
      .enter().append('path')
        .attr('class', 'country') 
        .attr('d', pathGenerator) // helps draw borders by setting 'd' attribute to country coordinates
      .append('title').text(d => countryName[d.id]); // label selection with country name
  });