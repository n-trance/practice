let animals = [
    {name: 'Alice', species: 'rabbit'},
    {name: 'Bob',   species: 'dog'},
    {name: 'Carlo', species: 'dog'},
    {name: 'Derek', species: 'cat'}
];

let names = animals.map(x => x.name);

let isDog = (animal => {
    return animal.species === 'dog'
});
let dogs = animals.filter(x => !isDog(x));

// console.log(names);
// console.log(dogs);

let orders = [
    {amount: 200},
    {amount: 250},
    {amount: 400},
    {amount: 100},
    {amount: 325}
];
let totalAmount = orders.reduce((sum, order) => {
    return sum + order.amount;
}, 0);
console.log(totalAmount);
