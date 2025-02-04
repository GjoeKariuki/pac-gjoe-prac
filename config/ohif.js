window.config = {
  routerBasename: "/",
  extensions: [],
  showStudyList: true,
  filterQueryParam: false,
  servers: {
    dicomWeb: [
      {
        name: "Orthanc",
        wadoUriRoot: "/orthanc/wado",
        qidoRoot: "/orthanc/dicom-web",
        wadoRoot: "/orthanc/dicom-web",
        qidoSupportsIncludeField: true,
        imageRendering: "wadors",
        thumbnailRendering: "wadors",
        enableStudyLazyLoad: true,
        supportsFuzzyMatching: true,
      },
    ],
  },
  whiteLabeling: {
    createLogoComponentFn: function (React) {
      return React.createElement("a", {
        target: "_self",
        rel: "noopener noreferrer",
        className: "header-brand",
        href: "/",
        style: {
          display: "block",
          background: "url(/logo.png)",
          backgroundSize: "contain",
          backgroundRepeat: "no-repeat",
          width: "200px",
        },
      });
    },
  },

  hotkeys: [
    {
      commandName: "incrementActiveViewport",
      label: "Next Viewport",
      keys: ["right"],
    },
    {
      commandName: "decrementActiveViewport",
      label: "Previous Viewport",
      keys: ["left"],
    },

    { commandName: "rotateViewportCW", label: "Rotate Right", keys: ["r"] },
    { commandName: "rotateViewportCCW", label: "Rotate Left", keys: ["l"] },
    { commandName: "invertViewport", label: "Invert", keys: ["i"] },
    {
      commandName: "flipViewportVertical",
      label: "Flip Horizontally",
      keys: ["h"],
    },
    {
      commandName: "flipViewportHorizontal",
      label: "Flip Vertically",
      keys: ["v"],
    },
    { commandName: "scaleUpViewport", label: "Zoom In", keys: ["+"] },
    { commandName: "scaleDownViewport", label: "Zoom Out", keys: ["-"] },
    { commandName: "fitViewportToWindow", label: "Zoom to Fit", keys: ["="] },
    { commandName: "resetViewport", label: "Reset", keys: ["space"] },

    { commandName: "nextImage", label: "Next Image", keys: ["down"] },
    { commandName: "previousImage", label: "Previous Image", keys: ["up"] },

    {
      commandName: "previousViewportDisplaySet",
      label: "Previous Series",
      keys: ["pagedown"],
    },
    {
      commandName: "nextViewportDisplaySet",
      label: "Next Series",
      keys: ["pageup"],
    },
    { commandName: "setZoomTool", label: "Zoom", keys: ["z"] },
    {
      commandName: "windowLevelPreset1",
      label: "W/L Preset 1",
      keys: ["1"],
    },
    {
      commandName: "windowLevelPreset2",
      label: "W/L Preset 2",
      keys: ["2"],
    },
    {
      commandName: "windowLevelPreset3",
      label: "W/L Preset 3",
      keys: ["3"],
    },
    {
      commandName: "windowLevelPreset4",
      label: "W/L Preset 4",
      keys: ["4"],
    },
    {
      commandName: "windowLevelPreset5",
      label: "W/L Preset 5",
      keys: ["5"],
    },
    {
      commandName: "windowLevelPreset6",
      label: "W/L Preset 6",
      keys: ["6"],
    },
    {
      commandName: "windowLevelPreset7",
      label: "W/L Preset 7",
      keys: ["7"],
    },
    {
      commandName: "windowLevelPreset8",
      label: "W/L Preset 8",
      keys: ["8"],
    },
    {
      commandName: "windowLevelPreset9",
      label: "W/L Preset 9",
      keys: ["9"],
    },
  ],
  cornerstoneExtensionConfig: {},

  studyListFunctionsEnabled: true,
};
