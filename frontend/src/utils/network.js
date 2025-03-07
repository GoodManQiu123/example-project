const defaultOptions = {
  nodes: {
    borderWidth: 0,
    borderWidthSelected: 2,
    size: 8,
    shape: 'dot',
    font: {
      size: 10,
      vadjust: -5, // vertical adjustment of the label
      face: 'Consolas',
    },
    color: '#154ec1'
  },
  edges: {
    font: {
      face: 'Consolas',
    },
    // apply smooth edges if needed
    // smooth: {
    //   type: 'cubicBezier',
    //   forceDirection: 'horizontal',
    //   roundness: 0.4,
    // },
    smooth: {
      type: 'continuous',
    },
    color: {
      color: '#d1d5db',
      highlight: '#154ec1',
    },
  },
  physics: false, // disable graph physics
};

// add received options to default options
export const generateOptions = (customOptions) => {
  if (customOptions === undefined) return defaultOptions;
  return {
    ...defaultOptions,
    ...customOptions,
    nodes: {
      ...defaultOptions.nodes,
      ...customOptions.nodes,
      font: {
        ...defaultOptions.nodes.font,
        ...customOptions.nodes?.font,
      },
    },
    edges: {
      ...defaultOptions.edges,
      ...customOptions.edges,
      font: {
        ...defaultOptions.edges.font,
        ...customOptions.edges?.font,
      },
      color: {
        ...defaultOptions.edges.color,
        ...customOptions.edges?.color,
      },
    },
  };
};

// convert list of author objects to string
export const authors2Str = (authors) => {
  if (authors.length === 0) return null;
  let str = '\nBy: ';
  for (let i = 0; i < authors.length - 1; i++) {
    str += authors[i].name + ', ';
  }
  str += authors[authors.length - 1].name;
  return str;
}
