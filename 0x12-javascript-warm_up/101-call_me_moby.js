#!/usr/bin/node

module.exports = {
    callMeMoby: (n, f) => {
        for (let i = 0; i < n; i++) {
            f();
        }
    }
};
