// src/api/ownersApi.js
import axios from 'axios';

const API_URL = 'http://localhost:8000/owners/'; // Replace with your actual API URL

export const fetchOwners = async () => {
    try {
        const response = await axios.get(API_URL);
        console.log(response);
        return response.data; // Returns the list of owners
    } catch (error) {
        console.error('Error fetching owners:', error);
        throw error;
    }
};

export const updateOwner = async (id, ownerData) => {
    try {
        const response = await axios.put(`${API_URL}${id}/`, ownerData);
        return response.data; // Returns the updated owner
    } catch (error) {
        console.error(`Error updating owner with ID ${id}:`, error);
        throw error;
    }
};

export const removeOwner = async (id) => {
    try {
        await axios.delete(`${API_URL}${id}/`);
        console.log(`Owner with ID ${id} removed successfully`);
    } catch (error) {
        console.error(`Error removing owner with ID ${id}:`, error);
        throw error;
    }
};
