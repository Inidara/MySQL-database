{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import mysql.connector"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "mydb = mysql.connector.connect(\n",
    "  host=\"localhost\",\n",
    "  user=\"root\",\n",
    "  password=\"Inidara\",\n",
    "  database=\"test\"\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('centable',)\n"
     ]
    }
   ],
   "source": [
    "mycursor = mydb.cursor()\n",
    "\n",
    "mycursor.execute(\"SHOW TABLES\")\n",
    "\n",
    "for x in mycursor:\n",
    "  print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('ABIA', 3.3, 37.6, 3.0, 0, 38.2)\n",
      "('ADAMAWA', 4.2, 5.7, 5.0, 0, 63.5)\n",
      "('AKWA IBOM', 15.3, 7.3, 15.4, 0, 35.9)\n",
      "('ANAMBRA', 6.9, 54.5, 14.0, 0, 14.2)\n",
      "('BAUCHI', 0.0, 0.6, 12.7, 0, 31.3)\n",
      "('BAYELSA', 9.0, 29.0, 17.6, 0, 0.0)\n",
      "('BENUE', 13.2, 13.0, 11.9, 0, 20.8)\n",
      "('BORNO', 0.2, 1.2, 18.7, 9, 42.0)\n",
      "('CROSS RIVER', 0.0, 34.4, 26.3, 0, 21.8)\n",
      "('DELTA', 3.4, 40.1, 28.8, 0, 19.5)\n",
      "('EBONYI', 0.0, 21.2, 12.0, 0, 14.8)\n",
      "('EDO', 16.5, 33.5, 18.9, 0, 18.6)\n",
      "('EKITI', 0.9, 29.0, 25.0, 0, 34.2)\n",
      "('ENUGU', 1.2, 50.9, 11.5, 0, 26.4)\n",
      "('GOMBE', 1.1, 0.4, 3.7, 0, 62.5)\n",
      "('IMO', 7.1, 35.3, 15.1, 0, 38.8)\n",
      "('JIGAWA', 2.2, 4.2, 5.0, 0, 37.4)\n",
      "('KADUNA', 0.0, 27.0, 8.6, 0, 44.1)\n",
      "('KANO', 0.4, 6.3, 9.5, 0, 55.5)\n",
      "('KATSINA', 0.0, 2.8, 10.0, 0, 56.9)\n",
      "('KEBBI', 0.0, 2.3, 11.5, 0, 33.5)\n",
      "('KOGI', 0.5, 48.2, 7.3, 0, 38.8)\n",
      "('KWARA', 0.0, 48.4, 14.7, 0, 31.2)\n",
      "('LAGOS', 1.4, 78.0, 10.7, 0, 6.0)\n",
      "('NASARAWA', 11.4, 20.4, 14.3, 0, 23.4)\n",
      "('NIGER', 11.1, 19.8, 34.0, 0, 21.8)\n",
      "('OGUN', 0.4, 31.5, 15.4, 0, 44.1)\n",
      "('ONDO', 12.2, 41.0, 20.5, 0, 21.2)\n",
      "('OSUN', 0.0, 47.0, 10.9, 0, 35.4)\n",
      "('OYO', 17.8, 32.7, 20.0, 0, 22.3)\n",
      "('PLATEAU', 12.4, 23.1, 19.7, 0, 27.2)\n",
      "('RIVERS', 21.7, 38.4, 11.3, 0, 9.3)\n",
      "('SOKOTO', 0.5, 2.3, 6.7, 0, 40.5)\n",
      "('TARABA', 3.0, 14.2, 6.7, 0, 36.1)\n",
      "('YOBE', 1.5, 0.9, 17.2, 0, 41.1)\n",
      "('ZAMFARA', 0.0, 1.1, 4.7, 0, 19.2)\n",
      "('FCT', 14.4, 29.9, 28.1, 0, 20.5)\n"
     ]
    }
   ],
   "source": [
    "mycursor = mydb.cursor()\n",
    "mycursor.execute(\"SELECT * FROM centable \")\n",
    "myresult = mycursor.fetchall()\n",
    "for x in myresult:\n",
    "    print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('IMO', 7.1, 35.3, 15.1, 0, 38.8)\n"
     ]
    }
   ],
   "source": [
    "mycursor = mydb.cursor()\n",
    "mycursor.execute(\"SELECT * FROM centable WHERE STATES='Imo'\")\n",
    "myresult = mycursor.fetchall()\n",
    "for x in myresult:\n",
    "    print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
