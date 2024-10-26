// src/api/flatsApi.js
import axios from 'axios';

const API_URL = 'http://localhost:8000/flats/';

export const fetchFlats = async () => {
    try {
        const response = await axios.get(API_URL);
        return response.data;
    } catch (error) {
        console.error('Error fetching flats:', error);
        throw error;
    }
};

export const updateFlats = async (id, flatData) => {
    try {
        const response = await axios.put(`${API_URL}${id}/`, flatData);
        return response.data;
    } catch (error) {
        console.error(`Error updating flat with ID ${id}:`, error);
        throw error;
    }
};

export const removeFlats = async (id) => {
    try {
        await axios.delete(`${API_URL}${id}/`);
        console.log(`flat with ID ${id} removed successfully`);
    } catch (error) {
        console.error(`Error removing flat with ID ${id}:`, error);
        throw error;
    }
};
