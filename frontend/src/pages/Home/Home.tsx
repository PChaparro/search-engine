import Styles from './Home.module.css';

import { SearchBar } from '../../components/SearchBar/SearchBar';

export const Home = () => {
  return (
    <main className={Styles.container}>
      <SearchBar />
      <p>Hello, this is the home page</p>
    </main>
  );
};
