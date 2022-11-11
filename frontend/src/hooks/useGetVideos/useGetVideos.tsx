import { useState } from 'react';
import { IVideo } from '../../interfaces/videos';
import { SearchVideosService } from '../../services/videos.services';

export const useGetVideos = () => {
  const [videos, setVideos] = useState(Array<IVideo>);
  const [isLoading, setIsLoading] = useState(false);

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
