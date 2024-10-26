// src/api/apartmentsApi.js
import axios from 'axios';

const API_URL = 'http://localhost:8000/apartments/';

export const fetchApartments = async () => {
    try {
        const response = await axios.get(API_URL);
        return response.data;
    } catch (error) {
        console.error('Error fetching apartments:', error);
        throw error;
    }
};

export const updateApartments = async (id, apartmentData) => {
    try {
        const response = await axios.put(`${API_URL}${id}/`, apartmentData);
        return response.data;
    } catch (error) {
        console.error(`Error updating apartment with ID ${id}:`, error);
        throw error;
    }
};

export const removeApartments = async (id) => {
    try {
        await axios.delete(`${API_URL}${id}/`);
        console.log(`apartment with ID ${id} removed successfully`);
    } catch (error) {
        console.error(`Error removing apartment with ID ${id}:`, error);
        throw error;
    }
};
