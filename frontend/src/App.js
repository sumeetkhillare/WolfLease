// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;


// src/App.js
// working
import React from 'react';
import ApartmentsComponent from './components/ApartmentsComponent';
import OwnersComponent from './components/OwnersComponent';

const App = () => {
    return (
        <div className="App">
            <OwnersComponent />
            <ApartmentsComponent/>
        </div>
    );
};

export default App;


// src/App.js
// import React from 'react';
// import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
// import LoginComponent from './components/LoginComponent';
// import OwnersComponent from './components/OwnersComponent'; // Other components...

// const App = () => {
//     return (
//         <Router>
//             <Routes>
//                 <Route path="/login" element={<LoginComponent />} />
//                 <Route path="/owners" element={<OwnersComponent />} />
//                 {/* Other routes can be added here */}
//             </Routes>
//         </Router>
//     );
// };

// export default App;

