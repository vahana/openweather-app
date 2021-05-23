import React, { useState, useEffect } from 'react';
import { useStateValue } from './store';
import { getWeather, updateWeather } from './reducers';

const API_URL = 'http://localhost:6543'

function isUSAZipCode(str)
{
  return /^\d{5}(-\d{4})?$/.test(str);
}

function CityInfo() {
    const [currentCity, setCurrentCity] = useState('');
    const [{city, latitude, longitude}, dispatch] = useStateValue();

    useEffect(() => {
        setCurrentCity(city);
    }, [city]);

    const onCityChange = (event) => {
        if (event.keyCode === 13) {
            event.preventDefault();
            let api = ''
            if (isUSAZipCode(currentCity)){
                api = `${API_URL}/zip?zip=${currentCity}`;
            }
            else{
                api = `${API_URL}/search?q=${currentCity}`;
            }
            getWeatherData(api);
        }
    };

    const getWeatherData = (api) => {
        getWeather(api)
        .then((data) => {
            setCurrentCity(data.name);
            updateWeather(dispatch, data);
        })
        .catch (e => {
            dispatch({
                type: "SET_ERROR",
                payload: {
                    error: e,
                    city: currentCity
                }
            });
        });
    };

    /**
     * Handle the input change
     */
    const handleChange = (event) => {
        setCurrentCity(event.target.value);
    }

    return (
        <div className="app-title">
            <p>Weather Info</p>
            <input type="text" placeholder="Enter the city or zip" autoComplete="off"
            onChange={handleChange}
            value={currentCity} onKeyUp={onCityChange} />
        </div>
    )
}

export default CityInfo;
