--
-- PostgreSQL database dump
--

\restrict BaNcFBlr1vmzZFw6Tw9Bz8rlldN4eaIrZqhhhdYRc957nPaOVhYgAe0hVenKpJJ

-- Dumped from database version 17.6
-- Dumped by pg_dump version 17.6

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

--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.categories (id, name, description, sort_order, is_active, created_on, updated_on) FROM stdin;
1	refrigerator	All refrigerators in one cat	1	1	2025-10-04 14:41:50.090957+05:30	2025-10-04 14:41:50.090957+05:30
2	television	All television in one cat	2	1	2025-10-04 14:42:10.468045+05:30	2025-10-04 14:42:10.468045+05:30
3	ac	All ac in one cat	3	1	2025-10-04 14:42:35.830121+05:30	2025-10-04 14:42:35.830121+05:30
4	smartphone	All smartphone in one cat	4	1	2025-10-04 14:43:02.661213+05:30	2025-10-04 14:43:02.661213+05:30
\.


--
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.products (id, name, description, category, price, quantity, created_on, updated_on) FROM stdin;
2	Samsung S26	latest samsung s26 phone	smartphone	3000	100	2025-10-16 12:40:37.07438+05:30	2025-10-16 12:40:37.07438+05:30
\.


--
-- Name: categories_sort_order_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.categories_sort_order_seq', 1, false);


--
-- Name: category_sort_order_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.category_sort_order_seq', 1, false);


--
-- Name: products_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.products_id_seq', 2, true);


--
-- PostgreSQL database dump complete
--

\unrestrict BaNcFBlr1vmzZFw6Tw9Bz8rlldN4eaIrZqhhhdYRc957nPaOVhYgAe0hVenKpJJ

