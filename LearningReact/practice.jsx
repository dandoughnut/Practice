const { render } = ReactDOM;

const Welcome = () => (
    <div id = "welcome">
        <h1>Hello World</h1>
    </div>
);

render(<Welcome />,
document.getElementById('target'));


const wSchools = schools.filter(school => school[0] === "w");

console.log(wSchools);
