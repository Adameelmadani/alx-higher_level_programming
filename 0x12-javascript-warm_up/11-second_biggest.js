#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  let m1 = 0;
  let m2 = 0;
  for (let i = 2; i < process.argv.length; i++) {
    if (i === 2) {
      m1 = Number(process.argv[i]);
    } else if (i === 3) {
      m2 = Number(process.argv[i]);
      if (m1 < m2) {
        m1 = m2;
        m2 = Number(process.argv[2]);
      }
    } else {
      if (Number(process.argv[i]) > m2 && Number(process.argv[i]) <= m1) {
        m2 = Number(process.argv[i]);
      } else if (Number(process.argv[i]) > m1) {
        m2 = m1;
        m1 = Number(process.argv[i]);
      }
    }
  }
  console.log(m2);
}
