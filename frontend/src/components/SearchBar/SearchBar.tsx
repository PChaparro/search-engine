import Styles from './SearchBar.module.css';

import { useRef } from 'react';

interface Props {
  searchCallback: (criteria: string) => Promise<void>;
}

export const SearchBar = ({ searchCallback }: Props) => {
  const searchBar = useRef<HTMLInputElement>(null);

  const HandleSubmit = () => {
    searchCallback(searchBar.current.value);
  };

  return (
    <header className={Styles.header}>
      <h1 className={Styles.header__title}>Search engine</h1>
      <form
        className={Styles.header__form}
        onSubmit={(e) => {
          e.preventDefault();
          HandleSubmit();
        }}
      >
        <div className={Styles.header__group}>
          <label htmlFor='criteria' hidden>
            Search criteria
          </label>
          <div className={Styles.header__wraper}>
            <input
              type='text'
              id='criteria'
              name='criteria'
              placeholder='Your search here'
              ref={searchBar}
              className={Styles.header__input}
            />
            <input type='submit' value='search' className={Styles.header__submit} />
          </div>
        </div>
      </form>
    </header>
  );
};
