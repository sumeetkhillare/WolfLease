// src/api/usersApi.js
import axios from 'axios';

const API_URL = 'http://localhost:8000/users/';

export const fetchusers = async () => {
    try {
        const response = await axios.get(API_URL);
        return response.data;
    } catch (error) {
        console.error('Error fetching users:', error);
        throw error;
    }
};

export const updateusers = async (id, userData) => {
    try {
        const response = await axios.put(`${API_URL}${id}/`, userData);
        return response.data;
    } catch (error) {
        console.error(`Error updating user with ID ${id}:`, error);
        throw error;
    }
};

export const removeusers = async (id) => {
    try {
        await axios.delete(`${API_URL}${id}/`);
        console.log(`user with ID ${id} removed successfully`);
    } catch (error) {
        console.error(`Error removing user with ID ${id}:`, error);
        throw error;
    }
};
