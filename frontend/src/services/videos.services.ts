import axios from 'axios';
import { IVideo } from '../interfaces/videos';

export const SearchVideosService = async (criteria: string): Promise<Array<IVideo>> => {
  try {
    const response = await axios.post('http://localhost:8080/search', { criteria });
    const videos = response.data.results;
    return videos;
  } catch {
    return [];
  }
};

export const GetRandomVideosService = async (): Promise<Array<IVideo>> => {
  try {
    const response = await axios.get('http://localhost:8080/random');
    const videos = response.data.results;
    return videos;
  } catch {
    return [];
  }
};
