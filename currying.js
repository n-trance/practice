let dragons = [
    { name: 'Alice',    element: 'fire' },
    { name: 'Bob',      element: 'water' },
    { name: 'Carl',     element: 'wind' },
    { name: 'Derek',    element: 'earth' },
    { name: 'Erika',    element: 'fire'}
];

// return true for dragons with element
let hasElement =
    (element, object) => object.element === element;

// return array of of fire dragons
let fireDragons =
    dragons.filter(x => hasElement('fire', x));

let jsonDragon = JSON.stringify(fireDragons, null, 2);
let parseDragon = JSON.parse(jsonDragon);

console.log(jsonDragon);
console.log(parseDragon);
