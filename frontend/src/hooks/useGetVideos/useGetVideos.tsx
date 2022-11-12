import { useState, useEffect } from 'react';
import { IVideo } from '../../interfaces/videos';
import { SearchVideosService, GetRandomVideosService } from '../../services/videos.services';

export const useGetVideos = () => {
  const [videos, setVideos] = useState(Array<IVideo>);
  const [isLoading, setIsLoading] = useState(false);

  // Get random videos on load
  useEffect(() => {
    const random = async () => {
      setIsLoading(true);
      const videos = await GetRandomVideosService();
      setVideos(videos);
      setIsLoading(false);
    };

    random();
  }, []);

  const search = async (criteria: string) => {
    setIsLoading(true);
    const videos = await SearchVideosService(criteria);
    setVideos(videos);
    setIsLoading(false);
  };

  return {
    videos,
    search,
    isLoading,
  };
};
