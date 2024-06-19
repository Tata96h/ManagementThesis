//"use client"

import DefaultLayout from '@/components/Layouts/DefaultLayout'

import { Employee } from "@/types/user";
import { columns } from "@/components/Tables/users-tables/columns";
import { EmployeeTable } from "@/components/Tables/users-tables/users-tables";
import { buttonVariants } from "@/components/ui/button";
import { Heading } from "@/components/ui/heading";
import { Separator } from "@/components/ui/separator";

import { cn } from "@/lib/utils";
import { Plus } from "lucide-react";
import Link from "next/link";


type paramsProps = {
  searchParams: {
    [key: string]: string | string[] | undefined;
  };
};

export default async function ListeEtudiant({ searchParams }: paramsProps) {
  
 const page = Number(searchParams.page) || 1;
  const pageLimit = Number(searchParams.limit) || 10;
  const country = searchParams.search || null;
  const offset = (page - 1) * pageLimit;

  const etuList = await fetch(
    `http://127.0.0.1:8000/etudiants/?offset=${offset}&limit=${pageLimit}`, { cache: 'no-store' }
  );
  console.log(etuList);
  
  // const res = await fetch(
  //   `https://api.slingacademy.com/v1/sample-data/users?offset=${offset}&limit=${pageLimit}` +
  //     (country ? `&search=${country}` : ""),
  // );
  
  const employeeRes = await etuList.json();
  const totalUsers = employeeRes.total_users; //1000
  const pageCount = Math.ceil(totalUsers / pageLimit);
  const employee: Employee[] = employeeRes.users;

 return (
 <DefaultLayout>
    {/* <div> {`Etudiants (${JSON.stringify(etuList.json())})`}  </div> */}
   <div className="flex flex-col gap-9">
        <div className="flex items-start justify-between">
          <Heading
            title={`Etudiants (${totalUsers})`}
            description="Nos étudiants"
          />

          <Link
            href={"/users/forms/etudiant"}
            className={cn(buttonVariants({ variant: "default" }))}
          >
            <Plus className="mr-2 h-4 w-4" /> Ajouter un nouveau étudiant
          </Link>
        </div>
        <Separator />

        <EmployeeTable
          searchKey=""
          pageNo={page}
          columns={columns}
          totalUsers={totalUsers}
          data={employee}
          pageCount={pageCount}
        />
  </div>

</DefaultLayout>

 )
};

