/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {

    let last = init
    return {
        increment:()=>{
            last+=1
            return last
        },
        decrement:()=>{
            last-=1
            return last   
        },reset:()=>{
            last=init
            return last
        }
    }
    
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */