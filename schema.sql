--
-- PostgreSQL database dump
--

-- Dumped from database version 17.5
-- Dumped by pg_dump version 17.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: books; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.books (
    id integer NOT NULL,
    title character varying(100),
    author character varying(100),
    genre character varying(50),
    year integer
);


ALTER TABLE public.books OWNER TO postgres;

--
-- Name: TABLE books; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.books IS 'id
title
author
genre
year';


--
-- Name: BooksInCollection_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."BooksInCollection_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."BooksInCollection_id_seq" OWNER TO postgres;

--
-- Name: BooksInCollection_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."BooksInCollection_id_seq" OWNED BY public.books.id;


--
-- Name: books id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.books ALTER COLUMN id SET DEFAULT nextval('public."BooksInCollection_id_seq"'::regclass);


--
-- Name: books BooksInCollection_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.books
    ADD CONSTRAINT "BooksInCollection_pkey" PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

