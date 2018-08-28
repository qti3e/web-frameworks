const physicalCpuCount = require('physical-cpu-count');
const { Storm } = require("@rayo/storm");

new Storm(() => require("./http"), {
  workers: physicalCpuCount,
  monitor: false
});
