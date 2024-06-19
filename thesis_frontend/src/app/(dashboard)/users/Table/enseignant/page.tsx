"use client"
import { useState } from 'react'
import { ChevronDownIcon } from '@heroicons/react/20/solid'
import { Field, Label, Switch } from '@headlessui/react'
import DefaultLayout from '@/components/Layouts/DefaultLayout'

function classNames(...classes: string[]) {
  return classes.filter(Boolean).join(' ')
}

export default function Example() {
  const [agreed, setAgreed] = useState(false)

  return (
        <DefaultLayout>

   <div className="flex flex-col gap-9">
  <div className="rounded-sm border border-stroke bg-white shadow-default dark:border-strokedark dark:bg-boxdark">
    <div className="border-b border-stroke px-6.5 py-4 dark:border-strokedark">
      <h3 className="font-medium text-black dark:text-white">Ajouter un étudiant</h3>
    </div>
    <form action="#">
      <div className="p-6.5">
        <div className="mb-4.5 flex flex-col gap-6 xl:flex-row">
          <div className="w-full xl:w-1/2">
            <label className="mb-3 block text-sm font-medium text-black dark:text-white">
Nom            </label>
            <input
              placeholder="Entrez votre nom"
              className="w-full rounded border-[1.5px] border-stroke bg-transparent px-5 py-3 text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary"
              type="text"
            />
          </div>
          <div className="w-full xl:w-1/2">
            <label className="mb-3 block text-sm font-medium text-black dark:text-white">
             Prénom
            </label>
            <input
              placeholder="Entrez votre prénom"
              className="w-full rounded border-[1.5px] border-stroke bg-transparent px-5 py-3 text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary"
              type="text"
            />
          </div>
        </div>
        <div className="mb-4.5 flex flex-col gap-6 xl:flex-row">
          <div className="w-full xl:w-1/2">
          <label className="mb-3 block text-sm font-medium text-black dark:text-white">
            Matricule <span className="text-meta-1">*</span>
          </label>
          <input
            placeholder="Entrez votre matricule"
            className="w-full rounded border-[1.5px] border-stroke bg-transparent px-5 py-3 text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary"
            type="number"
          />
          </div>
          <div className="w-full xl:w-1/2">
          <label className="mb-2.5 block text-black dark:text-white">
            Département{" "}
          </label>
          <div className="relative z-20 bg-transparent dark:bg-form-input">
            <select className="relative z-20 w-full appearance-none rounded border border-stroke bg-transparent px-5 py-3 outline-none transition focus:border-primary active:border-primary dark:border-form-strokedark dark:bg-form-input dark:focus:border-primary ">
              <option
                value=""
                className="text-body dark:text-bodydark"
              >
                Sélectionnez votre département
              </option>
              <option value="USA" className="text-body dark:text-bodydark">
                Informatique de Gestion
              </option>
              <option value="UK" className="text-body dark:text-bodydark">
                Statistiques
              </option>
              <option value="Canada" className="text-body dark:text-bodydark">
                Gestion commerciale
              </option>
            </select>
            <span className="absolute right-4 top-1/2 z-30 -translate-y-1/2">
              <svg
                className="fill-current"
                width={24}
                height={24}
                viewBox="0 0 24 24"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <g opacity="0.8">
                  <path
                    fillRule="evenodd"
                    clipRule="evenodd"
                    d="M5.29289 8.29289C5.68342 7.90237 6.31658 7.90237 6.70711 8.29289L12 13.5858L17.2929 8.29289C17.6834 7.90237 18.3166 7.90237 18.7071 8.29289C19.0976 8.68342 19.0976 9.31658 18.7071 9.70711L12.7071 15.7071C12.3166 16.0976 11.6834 16.0976 11.2929 15.7071L5.29289 9.70711C4.90237 9.31658 4.90237 8.68342 5.29289 8.29289Z"
                    fill=""
                  />
                </g>
              </svg>
            </span>
          </div>
        </div>
          
        </div>
        <div className="mb-4.5 flex flex-col gap-6 xl:flex-row">
                    <div className="w-full xl:w-1/2">

          <label className="mb-3 block text-sm font-medium text-black dark:text-white">
Grade           </label>
          <input
            placeholder="Entrez votre grade"
            className="w-full rounded border-[1.5px] border-stroke bg-transparent px-5 py-3 text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary"
            type="text"
          />
          </div>
                    <div className="w-full xl:w-1/2">

          <label className="mb-3 block text-sm font-medium text-black dark:text-white">
Spécialité          </label>
          <input
            placeholder="Entrez votre spécialité "
            className="w-full rounded border-[1.5px] border-stroke bg-transparent px-5 py-3 text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary"
            type="email"
          />
          </div>
        </div>
        <div className="mb-4.5 flex flex-col gap-6 xl:flex-row">
          <div className="w-full xl:w-1/2">
            <label className="mb-3 block text-sm font-medium text-black dark:text-white">
Mot de passe            </label>
            <input
              placeholder="Entrez votre mot de passe"
              className="w-full rounded border-[1.5px] border-stroke bg-transparent px-5 py-3 text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary"
              type="password"
            />
          </div>
          <div className="w-full xl:w-1/2">
            <label className="mb-3 block text-sm font-medium text-black dark:text-white">
             Mot de passe confirmé
            </label>
            <input
              placeholder="Confirmez votre mot de passe"
              className="w-full rounded border-[1.5px] border-stroke bg-transparent px-5 py-3 text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary"
              type="password"
            />
          </div>
        </div>
        <div className="mb-6">
          <label className="mb-3 block text-sm font-medium text-black dark:text-white">
            Biographie
          </label>
          <textarea
            rows={4}
            placeholder="Entrez votre biographie"
            className="w-full rounded border-[1.5px] border-stroke bg-transparent px-5 py-3 text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary"
            defaultValue={""}
          />
        </div>
        <button className="flex w-full justify-center rounded bg-primary p-3 font-medium text-gray hover:bg-opacity-90">
          Envoyez
        </button>
      </div>
    </form>
  </div>
</div>

            </DefaultLayout>

  )
}
