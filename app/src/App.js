import React from 'react';
import './App.css';
import { useStateValue } from './store';
import Notification from './Notification';
import WeatherInfo from './WeatherInfo';
import CityInfo from './CityInfo';

function App() {
  const [{error}, dispatch] = useStateValue();

  return (
    <div className="app">
      <CityInfo />
      {error && <Notification />}
      {!error && <WeatherInfo />}
    </div>
  );
}

export default App;
